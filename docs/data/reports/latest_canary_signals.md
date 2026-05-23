# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T16:22:19.801962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2037` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.0629` n `228`; crypto_major avg `-0.1515` n `8`; equity avg `-0.0472` n `67`; fx avg `0.0044` n `6`; index avg `-0.0302` n `23`; metal avg `-0.0224` n `18`; unknown avg `-0.0907` n `396`
- 1h: commodity avg `-0.1983` n `12`; crypto_alt avg `0.0221` n `228`; crypto_major avg `-0.1727` n `8`; equity avg `-0.033` n `67`; fx avg `0.0125` n `6`; index avg `-0.096` n `23`; metal avg `-0.0214` n `18`; unknown avg `0.266` n `396`
- 4h: commodity avg `-0.6397` n `12`; crypto_alt avg `2.363` n `228`; crypto_major avg `1.564` n `8`; equity avg `0.7818` n `67`; fx avg `0.0056` n `6`; index avg `0.2979` n `23`; metal avg `0.1919` n `18`; unknown avg `1.2366` n `396`
- 24h: commodity avg `0.0095` n `12`; crypto_alt avg `-2.9919` n `228`; crypto_major avg `-2.0001` n `8`; equity avg `-0.9332` n `67`; fx avg `0.0333` n `6`; index avg `-0.2111` n `23`; metal avg `-0.1762` n `18`; unknown avg `-1.6359` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0739`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0675`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0626`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `669`, weak_sample_signal
