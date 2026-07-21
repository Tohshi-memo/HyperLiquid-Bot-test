# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T21:22:32.278989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.0765` n `230`; crypto_major avg `0.0847` n `8`; equity avg `0.0439` n `98`; fx avg `-0.0038` n `6`; index avg `0.0135` n `25`; metal avg `0.004` n `20`; unknown avg `0.0039` n `771`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `0.1126` n `230`; crypto_major avg `0.1327` n `8`; equity avg `0.3101` n `98`; fx avg `-0.0243` n `6`; index avg `0.031` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0296` n `771`
- 4h: commodity avg `0.131` n `12`; crypto_alt avg `0.211` n `230`; crypto_major avg `-0.1302` n `8`; equity avg `0.5572` n `98`; fx avg `0.0116` n `6`; index avg `0.0233` n `25`; metal avg `0.0206` n `20`; unknown avg `-0.1645` n `771`
- 24h: commodity avg `0.5113` n `12`; crypto_alt avg `0.6639` n `230`; crypto_major avg `0.4704` n `8`; equity avg `4.4969` n `98`; fx avg `0.042` n `6`; index avg `0.6666` n `25`; metal avg `0.7327` n `20`; unknown avg `0.2245` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0837`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
