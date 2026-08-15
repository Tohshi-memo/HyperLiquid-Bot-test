# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T20:36:09.452778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0991` n `230`; crypto_major avg `-0.0564` n `8`; equity avg `0.0076` n `114`; fx avg `0.0043` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0852` n `791`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.1201` n `230`; crypto_major avg `-0.0604` n `8`; equity avg `0.0012` n `114`; fx avg `0.0055` n `6`; index avg `-0.0106` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0611` n `791`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `-0.1354` n `230`; crypto_major avg `0.0456` n `8`; equity avg `0.1055` n `114`; fx avg `0.0044` n `6`; index avg `-0.007` n `25`; metal avg `0.008` n `20`; unknown avg `1.8416` n `791`
- 24h: commodity avg `0.0126` n `12`; crypto_alt avg `0.8349` n `230`; crypto_major avg `0.5423` n `8`; equity avg `0.217` n `114`; fx avg `0.0049` n `6`; index avg `0.0` n `25`; metal avg `0.0423` n `20`; unknown avg `0.1208` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.22`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
