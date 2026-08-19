# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T04:22:29.361157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.0175` n `230`; crypto_major avg `0.0905` n `8`; equity avg `0.0484` n `120`; fx avg `0.0011` n `6`; index avg `0.0142` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.1026` n `789`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.1094` n `230`; crypto_major avg `0.0351` n `8`; equity avg `-0.1338` n `120`; fx avg `0.0095` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0095` n `20`; unknown avg `0.4936` n `789`
- 4h: commodity avg `0.0101` n `12`; crypto_alt avg `0.0381` n `230`; crypto_major avg `-0.1028` n `8`; equity avg `0.4678` n `120`; fx avg `-0.1302` n `6`; index avg `0.0397` n `25`; metal avg `0.017` n `20`; unknown avg `0.2241` n `789`
- 24h: commodity avg `0.2784` n `12`; crypto_alt avg `0.6576` n `230`; crypto_major avg `0.3861` n `8`; equity avg `-3.163` n `120`; fx avg `-0.1513` n `6`; index avg `-0.5178` n `25`; metal avg `-0.5267` n `20`; unknown avg `-0.1879` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
