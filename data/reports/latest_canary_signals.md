# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T04:41:46.668012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `0.1422` n `8`; equity avg `0.0604` n `113`; fx avg `-0.0028` n `6`; index avg `0.0104` n `25`; metal avg `0.021` n `20`; unknown avg `0.945` n `787`
- 1h: commodity avg `0.0648` n `12`; crypto_alt avg `0.0619` n `230`; crypto_major avg `0.1105` n `8`; equity avg `0.0068` n `113`; fx avg `-0.0026` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0818` n `20`; unknown avg `0.6412` n `786`
- 4h: commodity avg `0.0805` n `12`; crypto_alt avg `0.1424` n `230`; crypto_major avg `0.4387` n `8`; equity avg `0.2722` n `113`; fx avg `0.0353` n `6`; index avg `0.0434` n `25`; metal avg `-0.3335` n `20`; unknown avg `0.4787` n `786`
- 24h: commodity avg `-0.1711` n `12`; crypto_alt avg `-0.9874` n `230`; crypto_major avg `0.0852` n `8`; equity avg `2.4339` n `113`; fx avg `-0.0362` n `6`; index avg `0.2952` n `25`; metal avg `-0.1476` n `20`; unknown avg `0.1047` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2417`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
