# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T14:22:31.351589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `0.4766` n `228`; crypto_major avg `0.2465` n `8`; equity avg `0.0377` n `88`; fx avg `-0.0023` n `6`; index avg `0.0091` n `23`; metal avg `-0.0038` n `20`; unknown avg `0.2034` n `764`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `0.6259` n `228`; crypto_major avg `0.2714` n `8`; equity avg `0.0711` n `88`; fx avg `-0.0132` n `6`; index avg `-0.0076` n `23`; metal avg `0.0003` n `20`; unknown avg `0.214` n `764`
- 4h: commodity avg `0.1039` n `12`; crypto_alt avg `0.5411` n `228`; crypto_major avg `0.3696` n `8`; equity avg `0.0828` n `88`; fx avg `-0.0059` n `6`; index avg `0.0172` n `23`; metal avg `-0.0166` n `20`; unknown avg `-0.2541` n `764`
- 24h: commodity avg `0.1454` n `12`; crypto_alt avg `-0.246` n `228`; crypto_major avg `-1.1014` n `8`; equity avg `0.0001` n `88`; fx avg `-0.0107` n `6`; index avg `-0.0631` n `23`; metal avg `-0.0417` n `20`; unknown avg `15.5722` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
