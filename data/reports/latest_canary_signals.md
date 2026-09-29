# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T06:07:26.188172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0534` n `12`; crypto_alt avg `0.284` n `234`; crypto_major avg `0.4053` n `8`; equity avg `0.2408` n `141`; fx avg `-0.0122` n `6`; index avg `0.0414` n `26`; metal avg `0.021` n `20`; unknown avg `0.248` n `945`
- 1h: commodity avg `-0.0718` n `12`; crypto_alt avg `0.7221` n `234`; crypto_major avg `0.7479` n `8`; equity avg `0.2113` n `141`; fx avg `-0.0514` n `6`; index avg `0.0375` n `26`; metal avg `0.0627` n `20`; unknown avg `0.9784` n `945`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `1.2642` n `234`; crypto_major avg `1.0787` n `8`; equity avg `0.0468` n `141`; fx avg `-0.075` n `6`; index avg `-0.0372` n `26`; metal avg `0.0125` n `20`; unknown avg `0.9732` n `939`
- 24h: commodity avg `0.0025` n `12`; crypto_alt avg `-1.327` n `234`; crypto_major avg `0.1173` n `8`; equity avg `-1.9076` n `141`; fx avg `-0.1488` n `6`; index avg `-0.2073` n `26`; metal avg `-0.4007` n `20`; unknown avg `116.9863` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
