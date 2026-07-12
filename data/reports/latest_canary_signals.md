# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T11:07:24.707781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `-0.0619` n `230`; crypto_major avg `0.0457` n `8`; equity avg `0.013` n `92`; fx avg `0.0005` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.13` n `763`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `-0.0877` n `230`; crypto_major avg `0.0639` n `8`; equity avg `-0.0146` n `92`; fx avg `0.0029` n `6`; index avg `0.0019` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.0047` n `763`
- 4h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.0807` n `230`; crypto_major avg `0.1245` n `8`; equity avg `0.0298` n `92`; fx avg `0.0022` n `6`; index avg `0.0227` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0686` n `763`
- 24h: commodity avg `0.5487` n `12`; crypto_alt avg `-0.8843` n `230`; crypto_major avg `-0.7985` n `8`; equity avg `-0.2147` n `92`; fx avg `0.0095` n `6`; index avg `-0.1293` n `25`; metal avg `-0.1124` n `20`; unknown avg `0.0804` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1603`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1213`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1164`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1109`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1023`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1014`, n `669`, weak_sample_signal
