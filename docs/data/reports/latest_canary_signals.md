# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T11:22:25.256384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0882` n `230`; crypto_major avg `0.003` n `8`; equity avg `0.0475` n `92`; fx avg `0.0` n `6`; index avg `0.0025` n `25`; metal avg `0.0018` n `20`; unknown avg `0.002` n `765`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `-0.219` n `230`; crypto_major avg `-0.0431` n `8`; equity avg `0.0099` n `92`; fx avg `0.002` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.1523` n `763`
- 4h: commodity avg `0.1066` n `12`; crypto_alt avg `-0.2102` n `230`; crypto_major avg `0.0568` n `8`; equity avg `0.0644` n `92`; fx avg `0.0052` n `6`; index avg `0.0268` n `25`; metal avg `-0.0163` n `20`; unknown avg `-0.1226` n `763`
- 24h: commodity avg `0.5702` n `12`; crypto_alt avg `-0.9535` n `230`; crypto_major avg `-0.7408` n `8`; equity avg `-0.1514` n `92`; fx avg `0.002` n `6`; index avg `-0.1265` n `25`; metal avg `-0.113` n `20`; unknown avg `0.1172` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1602`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1212`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1166`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1106`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `669`, weak_sample_signal
