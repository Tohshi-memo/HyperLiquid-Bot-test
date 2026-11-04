# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T01:37:26.456437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.15` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.0048` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3681` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0454` n `13`; crypto_alt avg `-0.179` n `239`; crypto_major avg `-0.1729` n `8`; equity avg `-0.3061` n `158`; fx avg `-0.0497` n `6`; index avg `-0.0624` n `27`; metal avg `0.0448` n `20`; unknown avg `-0.0092` n `1264`
- 1h: commodity avg `-0.1355` n `13`; crypto_alt avg `-0.096` n `239`; crypto_major avg `-0.1244` n `8`; equity avg `-1.0475` n `158`; fx avg `-0.0616` n `6`; index avg `-0.217` n `27`; metal avg `0.3039` n `20`; unknown avg `0.2284` n `1258`
- 4h: commodity avg `-0.1816` n `13`; crypto_alt avg `-1.6178` n `239`; crypto_major avg `-1.8174` n `8`; equity avg `-2.7274` n `158`; fx avg `-0.0406` n `6`; index avg `-0.4493` n `27`; metal avg `0.1874` n `20`; unknown avg `171.5314` n `1194`
- 24h: commodity avg `0.1351` n `13`; crypto_alt avg `-0.1613` n `239`; crypto_major avg `-0.4584` n `8`; equity avg `-0.5119` n `158`; fx avg `0.0933` n `6`; index avg `-0.2529` n `27`; metal avg `-0.2532` n `20`; unknown avg `0.3626` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
