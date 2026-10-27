# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T21:52:28.691292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.209` n `238`; crypto_major avg `-0.2373` n `8`; equity avg `0.0372` n `154`; fx avg `0.0008` n `6`; index avg `0.0116` n `27`; metal avg `-0.0047` n `20`; unknown avg `3.0023` n `1238`
- 1h: commodity avg `-0.0064` n `13`; crypto_alt avg `0.3364` n `238`; crypto_major avg `0.2646` n `8`; equity avg `0.1816` n `154`; fx avg `0.0017` n `6`; index avg `0.02` n `27`; metal avg `0.022` n `20`; unknown avg `2.6792` n `1226`
- 4h: commodity avg `0.1583` n `13`; crypto_alt avg `0.562` n `238`; crypto_major avg `0.3578` n `8`; equity avg `-0.0388` n `154`; fx avg `-0.0189` n `6`; index avg `0.0173` n `27`; metal avg `0.09` n `20`; unknown avg `3.4066` n `1152`
- 24h: commodity avg `-0.1991` n `13`; crypto_alt avg `1.4064` n `237`; crypto_major avg `1.6447` n `8`; equity avg `1.4883` n `154`; fx avg `-0.0469` n `6`; index avg `0.4126` n `27`; metal avg `0.2341` n `20`; unknown avg `31.3415` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2304`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
