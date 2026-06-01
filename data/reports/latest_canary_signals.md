# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T23:52:20.233992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.9` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1586` n `12`; crypto_alt avg `-0.1407` n `228`; crypto_major avg `-0.0813` n `8`; equity avg `-0.1321` n `69`; fx avg `-0.0074` n `6`; index avg `-0.0736` n `23`; metal avg `0.0187` n `18`; unknown avg `0.0504` n `422`
- 1h: commodity avg `-0.3071` n `12`; crypto_alt avg `0.0662` n `228`; crypto_major avg `-0.0111` n `8`; equity avg `0.0085` n `69`; fx avg `0.0005` n `6`; index avg `-0.0436` n `23`; metal avg `0.0581` n `18`; unknown avg `0.1101` n `422`
- 4h: commodity avg `-0.1776` n `12`; crypto_alt avg `-0.4343` n `228`; crypto_major avg `0.0332` n `8`; equity avg `-0.2675` n `69`; fx avg `-0.0202` n `6`; index avg `-0.2366` n `23`; metal avg `0.059` n `18`; unknown avg `-0.107` n `422`
- 24h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.1377` n `228`; crypto_major avg `-0.8004` n `8`; equity avg `-0.3292` n `69`; fx avg `0.0456` n `6`; index avg `0.1021` n `23`; metal avg `-0.3752` n `18`; unknown avg `1.573` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
