# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T14:07:33.311438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-4.407` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.8962` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0456` n `12`; crypto_alt avg `-0.0915` n `230`; crypto_major avg `-0.1785` n `8`; equity avg `0.1981` n `102`; fx avg `-0.0166` n `6`; index avg `0.0167` n `25`; metal avg `-0.0177` n `20`; unknown avg `0.1562` n `779`
- 1h: commodity avg `0.1407` n `12`; crypto_alt avg `0.3186` n `230`; crypto_major avg `0.101` n `8`; equity avg `1.9972` n `102`; fx avg `-0.2713` n `6`; index avg `0.142` n `25`; metal avg `0.157` n `20`; unknown avg `0.0946` n `779`
- 4h: commodity avg `-0.2045` n `12`; crypto_alt avg `0.1839` n `230`; crypto_major avg `0.0977` n `8`; equity avg `4.5047` n `102`; fx avg `-0.3421` n `6`; index avg `0.511` n `25`; metal avg `0.2051` n `20`; unknown avg `0.1503` n `779`
- 24h: commodity avg `-0.0451` n `12`; crypto_alt avg `0.4238` n `230`; crypto_major avg `0.3575` n `8`; equity avg `2.4854` n `102`; fx avg `-0.3532` n `6`; index avg `0.1699` n `25`; metal avg `0.8084` n `20`; unknown avg `-0.1932` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
