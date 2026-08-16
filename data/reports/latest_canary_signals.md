# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T03:37:32.069243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0215` n `230`; crypto_major avg `-0.0138` n `8`; equity avg `0.0483` n `114`; fx avg `-0.0017` n `6`; index avg `0.0079` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0391` n `791`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0772` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `0.1094` n `114`; fx avg `-0.0046` n `6`; index avg `0.0074` n `25`; metal avg `0.014` n `20`; unknown avg `-0.0688` n `791`
- 4h: commodity avg `0.0525` n `12`; crypto_alt avg `-0.0925` n `230`; crypto_major avg `0.0762` n `8`; equity avg `0.1297` n `114`; fx avg `-0.0014` n `6`; index avg `0.0066` n `25`; metal avg `0.0231` n `20`; unknown avg `-0.0734` n `791`
- 24h: commodity avg `0.0045` n `12`; crypto_alt avg `0.0586` n `230`; crypto_major avg `-0.0862` n `8`; equity avg `0.2557` n `114`; fx avg `-0.042` n `6`; index avg `0.0082` n `25`; metal avg `0.0131` n `20`; unknown avg `-0.0057` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2224`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
