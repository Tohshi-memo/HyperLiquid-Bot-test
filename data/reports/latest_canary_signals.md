# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T18:52:25.753322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.171` n `13`; crypto_alt avg `0.3347` n `239`; crypto_major avg `0.3254` n `8`; equity avg `0.291` n `162`; fx avg `-0.005` n `6`; index avg `0.0172` n `27`; metal avg `0.0601` n `20`; unknown avg `0.2864` n `1266`
- 1h: commodity avg `-0.1682` n `13`; crypto_alt avg `0.327` n `239`; crypto_major avg `0.2208` n `8`; equity avg `-0.1784` n `162`; fx avg `-0.022` n `6`; index avg `-0.0206` n `27`; metal avg `-0.0377` n `20`; unknown avg `-0.0881` n `1263`
- 4h: commodity avg `-0.3924` n `13`; crypto_alt avg `-0.2136` n `239`; crypto_major avg `-0.3468` n `8`; equity avg `-0.9565` n `162`; fx avg `-0.0556` n `6`; index avg `-0.0786` n `27`; metal avg `-0.2916` n `20`; unknown avg `0.4418` n `1235`
- 24h: commodity avg `-1.1085` n `13`; crypto_alt avg `0.9197` n `239`; crypto_major avg `0.9115` n `8`; equity avg `-2.3452` n `162`; fx avg `-0.0989` n `6`; index avg `-0.2002` n `27`; metal avg `-0.2982` n `20`; unknown avg `249.3556` n `1037`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1329`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.103`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0889`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `669`, weak_sample_signal
