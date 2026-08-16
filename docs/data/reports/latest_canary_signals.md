# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T14:07:23.985517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0135` n `230`; crypto_major avg `0.0062` n `8`; equity avg `-0.0114` n `114`; fx avg `0.0007` n `6`; index avg `-0.0008` n `25`; metal avg `0.0093` n `20`; unknown avg `-0.0181` n `791`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0264` n `230`; crypto_major avg `0.0006` n `8`; equity avg `0.0239` n `114`; fx avg `-0.0067` n `6`; index avg `0.0046` n `25`; metal avg `0.0046` n `20`; unknown avg `0.0266` n `791`
- 4h: commodity avg `-0.007` n `12`; crypto_alt avg `0.0528` n `230`; crypto_major avg `0.0638` n `8`; equity avg `-0.0966` n `114`; fx avg `-0.0133` n `6`; index avg `0.0059` n `25`; metal avg `0.0003` n `20`; unknown avg `0.162` n `791`
- 24h: commodity avg `0.0495` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `0.0687` n `8`; equity avg `0.2274` n `114`; fx avg `-0.0185` n `6`; index avg `0.0387` n `25`; metal avg `0.0396` n `20`; unknown avg `0.1855` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
