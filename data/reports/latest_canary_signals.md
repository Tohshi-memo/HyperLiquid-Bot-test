# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T03:07:17.125097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0462` n `12`; crypto_alt avg `-0.0118` n `228`; crypto_major avg `-0.0775` n `8`; equity avg `-0.0085` n `66`; fx avg `0.0226` n `6`; index avg `0.0302` n `23`; metal avg `0.0428` n `18`; unknown avg `0.0368` n `383`
- 1h: commodity avg `0.1628` n `12`; crypto_alt avg `-0.0276` n `228`; crypto_major avg `0.0566` n `8`; equity avg `0.1393` n `66`; fx avg `0.0212` n `6`; index avg `0.0476` n `23`; metal avg `-0.2139` n `18`; unknown avg `-0.2752` n `383`
- 4h: commodity avg `0.2895` n `12`; crypto_alt avg `-0.3946` n `228`; crypto_major avg `-0.5234` n `8`; equity avg `-0.8395` n `66`; fx avg `0.1573` n `6`; index avg `-0.4924` n `23`; metal avg `-1.309` n `18`; unknown avg `-0.4535` n `383`
- 24h: commodity avg `0.2441` n `12`; crypto_alt avg `0.1621` n `228`; crypto_major avg `-0.2284` n `8`; equity avg `-0.9718` n `66`; fx avg `0.2435` n `6`; index avg `-0.2858` n `23`; metal avg `0.828` n `18`; unknown avg `0.1751` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
