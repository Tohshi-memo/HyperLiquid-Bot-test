# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T01:37:27.237775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6261` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5789` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.2061` n `230`; crypto_major avg `0.4677` n `8`; equity avg `-0.0039` n `121`; fx avg `0.0016` n `6`; index avg `0.0042` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.017` n `793`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `0.5553` n `230`; crypto_major avg `0.9636` n `8`; equity avg `-0.0504` n `121`; fx avg `0.0054` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0187` n `20`; unknown avg `0.6609` n `793`
- 4h: commodity avg `-0.0342` n `12`; crypto_alt avg `1.7863` n `230`; crypto_major avg `1.5879` n `8`; equity avg `0.009` n `121`; fx avg `-0.0054` n `6`; index avg `0.0211` n `25`; metal avg `-0.0382` n `20`; unknown avg `0.4958` n `793`
- 24h: commodity avg `0.0346` n `12`; crypto_alt avg `9.302` n `230`; crypto_major avg `6.789` n `8`; equity avg `0.5691` n `121`; fx avg `0.0472` n `6`; index avg `0.0656` n `25`; metal avg `0.275` n `20`; unknown avg `1.8283` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
