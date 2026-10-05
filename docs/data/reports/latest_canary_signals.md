# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T21:37:30.879369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `13`; crypto_alt avg `0.0251` n `235`; crypto_major avg `0.0219` n `8`; equity avg `-0.0164` n `144`; fx avg `-0.0208` n `6`; index avg `0.0128` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.1193` n `1079`
- 1h: commodity avg `-0.0276` n `13`; crypto_alt avg `0.3916` n `235`; crypto_major avg `0.1627` n `8`; equity avg `0.0377` n `144`; fx avg `-0.0091` n `6`; index avg `0.024` n `26`; metal avg `0.0111` n `20`; unknown avg `2.1442` n `1049`
- 4h: commodity avg `-0.0664` n `13`; crypto_alt avg `1.3135` n `235`; crypto_major avg `0.6825` n `8`; equity avg `0.1424` n `144`; fx avg `-0.0063` n `6`; index avg `0.0462` n `26`; metal avg `0.0938` n `20`; unknown avg `2.1718` n `1003`
- 24h: commodity avg `-0.3725` n `13`; crypto_alt avg `0.9155` n `235`; crypto_major avg `0.1864` n `8`; equity avg `0.3296` n `144`; fx avg `-0.111` n `6`; index avg `0.1412` n `26`; metal avg `0.177` n `20`; unknown avg `611.8431` n `818`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1996`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.18`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1712`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1261`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `670`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `670`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `670`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `670`, weak_sample_signal
