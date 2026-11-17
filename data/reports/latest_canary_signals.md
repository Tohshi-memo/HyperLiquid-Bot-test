# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T16:37:36.797429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3111` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0508` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0907` n `13`; crypto_alt avg `-0.4624` n `239`; crypto_major avg `-0.4769` n `8`; equity avg `-0.1551` n `163`; fx avg `-0.0159` n `6`; index avg `-0.0156` n `27`; metal avg `0.0119` n `20`; unknown avg `-0.2691` n `1263`
- 1h: commodity avg `0.1132` n `13`; crypto_alt avg `-0.8063` n `239`; crypto_major avg `-1.0996` n `8`; equity avg `-0.3904` n `163`; fx avg `0.0181` n `6`; index avg `-0.0488` n `27`; metal avg `-0.0916` n `20`; unknown avg `0.8801` n `1245`
- 4h: commodity avg `0.0517` n `13`; crypto_alt avg `-1.4512` n `239`; crypto_major avg `-1.5714` n `8`; equity avg `-2.808` n `163`; fx avg `0.0379` n `6`; index avg `-0.2603` n `27`; metal avg `-0.1049` n `20`; unknown avg `8.3318` n `1209`
- 24h: commodity avg `-0.0863` n `13`; crypto_alt avg `-0.2169` n `239`; crypto_major avg `-0.2544` n `8`; equity avg `-2.9995` n `163`; fx avg `-0.0055` n `6`; index avg `-0.3735` n `27`; metal avg `-0.0097` n `20`; unknown avg `8.3934` n `1098`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
