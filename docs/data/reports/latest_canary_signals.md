# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T16:07:19.626967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3839` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5059` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1896` n `12`; crypto_alt avg `0.179` n `228`; crypto_major avg `0.1899` n `8`; equity avg `0.0535` n `67`; fx avg `-0.0074` n `6`; index avg `-0.0599` n `23`; metal avg `0.0122` n `18`; unknown avg `0.2003` n `396`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `0.0312` n `228`; crypto_major avg `0.0057` n `8`; equity avg `0.034` n `67`; fx avg `0.007` n `6`; index avg `-0.1504` n `23`; metal avg `0.0528` n `18`; unknown avg `0.4403` n `396`
- 4h: commodity avg `-0.6637` n `12`; crypto_alt avg `2.4278` n `228`; crypto_major avg `1.7202` n `8`; equity avg `0.8286` n `67`; fx avg `0.0012` n `6`; index avg `0.3278` n `23`; metal avg `0.2143` n `18`; unknown avg `1.4721` n `396`
- 24h: commodity avg `-0.0675` n `12`; crypto_alt avg `-3.1204` n `228`; crypto_major avg `-1.8671` n `8`; equity avg `-0.95` n `67`; fx avg `0.0337` n `6`; index avg `-0.1918` n `23`; metal avg `-0.2042` n `18`; unknown avg `-1.7206` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0729`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0682`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0674`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0648`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0625`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `669`, weak_sample_signal
