# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T19:39:35.226506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0827` n `230`; crypto_major avg `0.0436` n `8`; equity avg `0.0025` n `114`; fx avg `-0.0043` n `6`; index avg `0.0114` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0023` n `791`
- 1h: commodity avg `0.0403` n `12`; crypto_alt avg `0.0941` n `230`; crypto_major avg `0.1716` n `8`; equity avg `0.0323` n `114`; fx avg `0.0001` n `6`; index avg `0.0283` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.1472` n `791`
- 4h: commodity avg `0.0787` n `12`; crypto_alt avg `-0.1479` n `230`; crypto_major avg `0.0975` n `8`; equity avg `0.0538` n `114`; fx avg `0.0002` n `6`; index avg `0.0206` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.146` n `791`
- 24h: commodity avg `0.0548` n `12`; crypto_alt avg `-0.2446` n `230`; crypto_major avg `0.075` n `8`; equity avg `0.2727` n `114`; fx avg `-0.0051` n `6`; index avg `0.0396` n `25`; metal avg `0.055` n `20`; unknown avg `0.1695` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2153`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
