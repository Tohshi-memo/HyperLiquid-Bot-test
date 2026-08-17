# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T07:52:26.075364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `12`; crypto_alt avg `0.0046` n `230`; crypto_major avg `-0.0389` n `8`; equity avg `0.0414` n `114`; fx avg `0.005` n `6`; index avg `0.0107` n `25`; metal avg `-0.0472` n `20`; unknown avg `-0.0045` n `792`
- 1h: commodity avg `0.0375` n `12`; crypto_alt avg `-0.1631` n `230`; crypto_major avg `-0.1206` n `8`; equity avg `0.0637` n `114`; fx avg `0.0114` n `6`; index avg `0.0023` n `25`; metal avg `0.0022` n `20`; unknown avg `0.0144` n `792`
- 4h: commodity avg `-0.0775` n `12`; crypto_alt avg `0.1041` n `230`; crypto_major avg `0.1513` n `8`; equity avg `0.567` n `114`; fx avg `0.01` n `6`; index avg `0.0926` n `25`; metal avg `0.0976` n `20`; unknown avg `0.0383` n `776`
- 24h: commodity avg `-0.2094` n `12`; crypto_alt avg `0.1969` n `230`; crypto_major avg `0.8312` n `8`; equity avg `1.2332` n `114`; fx avg `-0.0211` n `6`; index avg `0.1546` n `25`; metal avg `0.2786` n `20`; unknown avg `0.1205` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
