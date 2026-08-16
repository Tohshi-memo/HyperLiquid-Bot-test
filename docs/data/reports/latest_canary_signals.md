# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T16:22:24.305663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0225` n `230`; crypto_major avg `0.1014` n `8`; equity avg `0.0234` n `114`; fx avg `-0.0024` n `6`; index avg `0.0019` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.1107` n `791`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.1244` n `230`; crypto_major avg `0.1897` n `8`; equity avg `0.0418` n `114`; fx avg `-0.0017` n `6`; index avg `0.0059` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.045` n `791`
- 4h: commodity avg `-0.0113` n `12`; crypto_alt avg `0.2447` n `230`; crypto_major avg `0.3387` n `8`; equity avg `0.0394` n `114`; fx avg `0.002` n `6`; index avg `-0.005` n `25`; metal avg `-0.006` n `20`; unknown avg `0.0698` n `791`
- 24h: commodity avg `0.0598` n `12`; crypto_alt avg `-0.1181` n `230`; crypto_major avg `0.1627` n `8`; equity avg `0.3189` n `114`; fx avg `-0.0051` n `6`; index avg `0.0287` n `25`; metal avg `0.0409` n `20`; unknown avg `0.1149` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
