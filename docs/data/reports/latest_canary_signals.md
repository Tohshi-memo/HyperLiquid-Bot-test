# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T22:52:28.482061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0367` n `230`; crypto_major avg `-0.0808` n `8`; equity avg `-0.0198` n `98`; fx avg `-0.0038` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.0174` n `771`
- 1h: commodity avg `0.0216` n `12`; crypto_alt avg `-0.2481` n `230`; crypto_major avg `-0.1772` n `8`; equity avg `-0.1986` n `98`; fx avg `-0.0041` n `6`; index avg `-0.0285` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.1943` n `771`
- 4h: commodity avg `0.0699` n `12`; crypto_alt avg `-0.1534` n `230`; crypto_major avg `-0.1387` n `8`; equity avg `0.7139` n `98`; fx avg `-0.0143` n `6`; index avg `0.0108` n `25`; metal avg `-0.0324` n `20`; unknown avg `-0.2415` n `771`
- 24h: commodity avg `0.4635` n `12`; crypto_alt avg `0.9754` n `230`; crypto_major avg `0.814` n `8`; equity avg `4.3193` n `98`; fx avg `0.0629` n `6`; index avg `0.6893` n `25`; metal avg `0.8014` n `20`; unknown avg `0.1681` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0903`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0514`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0477`, n `666`, weak_sample_signal
