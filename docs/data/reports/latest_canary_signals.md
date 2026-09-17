# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T20:52:30.356563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.0315` n `234`; crypto_major avg `-0.0859` n `8`; equity avg `-0.0162` n `140`; fx avg `-0.0006` n `6`; index avg `0.0012` n `26`; metal avg `-0.0046` n `20`; unknown avg `67.8651` n `907`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.2042` n `234`; crypto_major avg `0.0666` n `8`; equity avg `0.038` n `140`; fx avg `-0.0068` n `6`; index avg `-0.0304` n `26`; metal avg `-0.0449` n `20`; unknown avg `18.4194` n `873`
- 4h: commodity avg `-0.183` n `12`; crypto_alt avg `0.2978` n `234`; crypto_major avg `0.2265` n `8`; equity avg `-0.0681` n `140`; fx avg `0.0035` n `6`; index avg `-0.037` n `26`; metal avg `-0.1896` n `20`; unknown avg `4.4626` n `873`
- 24h: commodity avg `-0.1999` n `12`; crypto_alt avg `4.0398` n `234`; crypto_major avg `1.8006` n `8`; equity avg `2.4193` n `138`; fx avg `-0.025` n `6`; index avg `0.4438` n `26`; metal avg `0.547` n `20`; unknown avg `6.1214` n `771`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
