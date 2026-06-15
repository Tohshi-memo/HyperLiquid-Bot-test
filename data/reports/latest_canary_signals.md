# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T20:08:25.514521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `0.3633` n `228`; crypto_major avg `0.1286` n `8`; equity avg `0.0759` n `77`; fx avg `-0.0082` n `6`; index avg `0.0516` n `23`; metal avg `0.0366` n `18`; unknown avg `-0.1304` n `687`
- 1h: commodity avg `0.2108` n `12`; crypto_alt avg `-0.6352` n `228`; crypto_major avg `-0.5275` n `8`; equity avg `0.1203` n `77`; fx avg `-0.0174` n `6`; index avg `0.0675` n `23`; metal avg `0.0177` n `18`; unknown avg `0.2262` n `687`
- 4h: commodity avg `0.7653` n `12`; crypto_alt avg `-1.4644` n `228`; crypto_major avg `-0.4776` n `8`; equity avg `-0.0883` n `77`; fx avg `-0.0349` n `6`; index avg `-0.1265` n `23`; metal avg `-0.5023` n `18`; unknown avg `3.4783` n `687`
- 24h: commodity avg `-0.4348` n `12`; crypto_alt avg `5.1317` n `228`; crypto_major avg `6.9328` n `8`; equity avg `3.0371` n `76`; fx avg `0.0288` n `6`; index avg `1.3023` n `23`; metal avg `2.1832` n `18`; unknown avg `4.7693` n `527`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
