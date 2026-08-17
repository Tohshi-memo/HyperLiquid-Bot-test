# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T01:37:27.178512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0833` n `12`; crypto_alt avg `0.0599` n `230`; crypto_major avg `0.1168` n `8`; equity avg `-0.1168` n `114`; fx avg `-0.0031` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0882` n `20`; unknown avg `-0.1058` n `792`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `0.6077` n `230`; crypto_major avg `0.8689` n `8`; equity avg `0.1385` n `114`; fx avg `-0.0417` n `6`; index avg `-0.0025` n `25`; metal avg `0.1208` n `20`; unknown avg `0.6046` n `792`
- 4h: commodity avg `-0.1354` n `12`; crypto_alt avg `0.1572` n `230`; crypto_major avg `0.3799` n `8`; equity avg `0.0945` n `114`; fx avg `-0.0633` n `6`; index avg `0.0166` n `25`; metal avg `0.2232` n `20`; unknown avg `-0.1608` n `791`
- 24h: commodity avg `-0.1089` n `12`; crypto_alt avg `0.0304` n `230`; crypto_major avg `0.3694` n `8`; equity avg `0.4058` n `114`; fx avg `-0.0638` n `6`; index avg `0.039` n `25`; metal avg `0.226` n `20`; unknown avg `-0.0009` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
