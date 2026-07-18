# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T21:07:24.678063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.1133` n `8`; equity avg `-0.0008` n `96`; fx avg `0.0007` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.0362` n `770`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `0.0562` n `230`; crypto_major avg `0.1377` n `8`; equity avg `0.0013` n `96`; fx avg `0.0108` n `6`; index avg `-0.0106` n `25`; metal avg `0.0086` n `20`; unknown avg `0.0512` n `770`
- 4h: commodity avg `0.1998` n `12`; crypto_alt avg `0.2017` n `230`; crypto_major avg `0.4535` n `8`; equity avg `0.0075` n `96`; fx avg `-0.0085` n `6`; index avg `-0.0262` n `25`; metal avg `-0.0184` n `20`; unknown avg `0.039` n `770`
- 24h: commodity avg `0.3145` n `12`; crypto_alt avg `-0.395` n `230`; crypto_major avg `0.3431` n `8`; equity avg `-0.2515` n `96`; fx avg `-0.0927` n `6`; index avg `0.0289` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0409` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
