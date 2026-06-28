# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T11:37:26.040737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `-0.151` n `228`; crypto_major avg `-0.1228` n `8`; equity avg `-0.024` n `88`; fx avg `0.005` n `6`; index avg `-0.008` n `23`; metal avg `-0.0021` n `20`; unknown avg `-0.0325` n `764`
- 1h: commodity avg `0.0689` n `12`; crypto_alt avg `0.2554` n `228`; crypto_major avg `0.4387` n `8`; equity avg `0.0662` n `88`; fx avg `0.0015` n `6`; index avg `0.0114` n `23`; metal avg `0.008` n `20`; unknown avg `-0.4706` n `764`
- 4h: commodity avg `-0.0513` n `12`; crypto_alt avg `0.147` n `228`; crypto_major avg `0.3396` n `8`; equity avg `0.2` n `88`; fx avg `0.0075` n `6`; index avg `0.062` n `23`; metal avg `0.0112` n `20`; unknown avg `2.332` n `742`
- 24h: commodity avg `0.1759` n `12`; crypto_alt avg `0.1689` n `228`; crypto_major avg `-0.3573` n `8`; equity avg `0.1256` n `88`; fx avg `-0.0032` n `6`; index avg `-0.0399` n `23`; metal avg `0.0001` n `20`; unknown avg `15.6224` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2119`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
