# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T08:37:26.222088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1138` n `12`; crypto_alt avg `0.1813` n `230`; crypto_major avg `0.1451` n `8`; equity avg `0.1422` n `113`; fx avg `-0.0308` n `6`; index avg `0.0153` n `25`; metal avg `0.0599` n `20`; unknown avg `0.0346` n `787`
- 1h: commodity avg `-0.0705` n `12`; crypto_alt avg `0.1896` n `230`; crypto_major avg `0.098` n `8`; equity avg `0.3587` n `113`; fx avg `-0.0704` n `6`; index avg `0.0363` n `25`; metal avg `0.0709` n `20`; unknown avg `-0.0567` n `787`
- 4h: commodity avg `0.1824` n `12`; crypto_alt avg `-0.2384` n `230`; crypto_major avg `-0.3764` n `8`; equity avg `0.2971` n `113`; fx avg `-0.0396` n `6`; index avg `0.0565` n `25`; metal avg `0.196` n `20`; unknown avg `-0.0646` n `755`
- 24h: commodity avg `0.0216` n `12`; crypto_alt avg `-0.5441` n `230`; crypto_major avg `-0.7386` n `8`; equity avg `1.8077` n `113`; fx avg `-0.1108` n `6`; index avg `0.3484` n `25`; metal avg `-0.0602` n `20`; unknown avg `0.8812` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
