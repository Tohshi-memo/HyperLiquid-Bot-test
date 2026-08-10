# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T00:52:26.626834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.1712` n `230`; crypto_major avg `0.1201` n `8`; equity avg `0.0287` n `112`; fx avg `-0.0032` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.0226` n `785`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `0.4598` n `230`; crypto_major avg `0.2666` n `8`; equity avg `-0.0626` n `112`; fx avg `0.069` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0699` n `20`; unknown avg `0.14` n `785`
- 4h: commodity avg `0.3145` n `12`; crypto_alt avg `-0.6492` n `230`; crypto_major avg `-0.6719` n `8`; equity avg `-0.3158` n `112`; fx avg `0.0569` n `6`; index avg `-0.036` n `25`; metal avg `-0.2336` n `20`; unknown avg `0.372` n `785`
- 24h: commodity avg `0.4973` n `12`; crypto_alt avg `0.7991` n `230`; crypto_major avg `-0.2999` n `8`; equity avg `-0.1192` n `112`; fx avg `0.066` n `6`; index avg `-0.0151` n `25`; metal avg `-0.162` n `20`; unknown avg `-0.4059` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
