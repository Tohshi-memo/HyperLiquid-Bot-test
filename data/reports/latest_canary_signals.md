# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T10:37:30.940870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1779` n `12`; crypto_alt avg `0.103` n `228`; crypto_major avg `0.1349` n `8`; equity avg `0.0227` n `74`; fx avg `0.0018` n `6`; index avg `0.0309` n `23`; metal avg `0.0601` n `18`; unknown avg `-1.6691` n `556`
- 1h: commodity avg `-0.3474` n `12`; crypto_alt avg `-0.0327` n `228`; crypto_major avg `-0.019` n `8`; equity avg `0.1784` n `74`; fx avg `-0.0269` n `6`; index avg `0.0559` n `23`; metal avg `0.0634` n `18`; unknown avg `-1.8165` n `556`
- 4h: commodity avg `-0.744` n `12`; crypto_alt avg `0.0368` n `228`; crypto_major avg `0.0003` n `8`; equity avg `0.7661` n `74`; fx avg `-0.0676` n `6`; index avg `0.3682` n `23`; metal avg `-0.0601` n `18`; unknown avg `0.6512` n `548`
- 24h: commodity avg `0.0358` n `12`; crypto_alt avg `1.5335` n `228`; crypto_major avg `1.4939` n `8`; equity avg `1.0511` n `74`; fx avg `-0.0084` n `6`; index avg `0.142` n `23`; metal avg `-0.4972` n `18`; unknown avg `4.4942` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
