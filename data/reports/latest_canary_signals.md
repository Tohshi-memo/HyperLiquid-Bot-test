# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T07:37:27.551643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2969` n `12`; crypto_alt avg `0.0733` n `228`; crypto_major avg `0.2436` n `8`; equity avg `-0.0033` n `74`; fx avg `0.0179` n `6`; index avg `-0.003` n `23`; metal avg `-0.1219` n `18`; unknown avg `0.0333` n `547`
- 1h: commodity avg `0.6693` n `12`; crypto_alt avg `0.799` n `228`; crypto_major avg `0.7927` n `8`; equity avg `-0.053` n `74`; fx avg `0.0366` n `6`; index avg `-0.0314` n `23`; metal avg `-0.2992` n `18`; unknown avg `0.1485` n `547`
- 4h: commodity avg `0.1229` n `12`; crypto_alt avg `0.2447` n `228`; crypto_major avg `-0.042` n `8`; equity avg `-0.0429` n `74`; fx avg `0.1025` n `6`; index avg `-0.1669` n `23`; metal avg `0.3572` n `18`; unknown avg `-0.7557` n `537`
- 24h: commodity avg `-0.3919` n `12`; crypto_alt avg `-1.0008` n `228`; crypto_major avg `-3.2074` n `8`; equity avg `-3.4441` n `74`; fx avg `0.2088` n `6`; index avg `-1.6651` n `23`; metal avg `-2.8068` n `18`; unknown avg `-0.0466` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
