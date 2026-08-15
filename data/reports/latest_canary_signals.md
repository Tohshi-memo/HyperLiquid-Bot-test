# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T10:07:27.110242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `0.0299` n `230`; crypto_major avg `-0.0245` n `8`; equity avg `-0.023` n `114`; fx avg `-0.009` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.067` n `791`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `0.124` n `230`; crypto_major avg `0.105` n `8`; equity avg `0.025` n `114`; fx avg `-0.007` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.0273` n `791`
- 4h: commodity avg `-0.1838` n `12`; crypto_alt avg `0.0562` n `230`; crypto_major avg `-0.1369` n `8`; equity avg `0.0354` n `114`; fx avg `-0.02` n `6`; index avg `-0.0017` n `25`; metal avg `0.0086` n `20`; unknown avg `0.0823` n `791`
- 24h: commodity avg `-0.0237` n `12`; crypto_alt avg `1.144` n `230`; crypto_major avg `0.0311` n `8`; equity avg `-0.5831` n `114`; fx avg `0.137` n `6`; index avg `-0.1559` n `25`; metal avg `0.1699` n `20`; unknown avg `-0.0632` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
