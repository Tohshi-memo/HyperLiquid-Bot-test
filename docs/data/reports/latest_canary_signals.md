# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T10:37:27.398683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.1607` n `228`; crypto_major avg `-0.2098` n `8`; equity avg `-0.0148` n `88`; fx avg `0.0019` n `6`; index avg `0.0007` n `23`; metal avg `-0.0081` n `20`; unknown avg `0.078` n `764`
- 1h: commodity avg `-0.0282` n `12`; crypto_alt avg `-0.4374` n `228`; crypto_major avg `-0.5096` n `8`; equity avg `-0.1023` n `88`; fx avg `0.0008` n `6`; index avg `-0.0113` n `23`; metal avg `-0.0139` n `20`; unknown avg `1.9296` n `750`
- 4h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.2873` n `228`; crypto_major avg `0.3304` n `8`; equity avg `0.2244` n `88`; fx avg `0.0244` n `6`; index avg `0.0562` n `23`; metal avg `-0.0065` n `20`; unknown avg `-0.2458` n `742`
- 24h: commodity avg `0.128` n `12`; crypto_alt avg `-0.347` n `228`; crypto_major avg `-1.088` n `8`; equity avg `0.0283` n `88`; fx avg `0.0059` n `6`; index avg `-0.0744` n `23`; metal avg `-0.0196` n `20`; unknown avg `16.243` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2166`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
