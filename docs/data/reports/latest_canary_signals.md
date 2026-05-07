# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T06:22:14.360521+00:00`
- Correlation status: `ready`
- Asset price records: `525`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1736` n `12`; crypto_alt avg `-0.2514` n `228`; crypto_major avg `-0.1353` n `8`; equity avg `0.0045` n `65`; fx avg `0.0476` n `4`; index avg `-0.0094` n `23`; metal avg `0.16` n `18`; unknown avg `-0.0407` n `358`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.2475` n `228`; crypto_major avg `-0.05` n `8`; equity avg `0.0777` n `65`; fx avg `0.047` n `4`; index avg `0.0461` n `23`; metal avg `0.3979` n `18`; unknown avg `-0.0299` n `356`
- 4h: commodity avg `0.0151` n `12`; crypto_alt avg `1.0236` n `228`; crypto_major avg `0.2417` n `8`; equity avg `0.5038` n `65`; fx avg `0.0794` n `4`; index avg `0.1555` n `23`; metal avg `0.2933` n `18`; unknown avg `0.1982` n `356`
- 24h: commodity avg `-1.7648` n `7`; crypto_alt avg `1.1525` n `223`; crypto_major avg `-0.9841` n `7`; equity avg `1.3433` n `47`; fx avg `0.0666` n `4`; index avg `1.0936` n `6`; metal avg `1.7887` n `7`; unknown avg `1.389` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1224`, n `521`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `521`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0844`, n `517`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `517`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `521`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.076`, n `517`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0737`, n `517`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `517`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0689`, n `517`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `521`, weak_sample_signal
