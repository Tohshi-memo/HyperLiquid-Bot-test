# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T13:52:35.855268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2393` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `0.0353` n `229`; crypto_major avg `0.0757` n `8`; equity avg `0.7949` n `88`; fx avg `-0.0078` n `6`; index avg `0.1128` n `25`; metal avg `0.165` n `20`; unknown avg `0.1887` n `763`
- 1h: commodity avg `0.1384` n `12`; crypto_alt avg `0.6614` n `229`; crypto_major avg `0.9682` n `8`; equity avg `0.6168` n `88`; fx avg `-0.011` n `6`; index avg `0.0702` n `25`; metal avg `0.2698` n `20`; unknown avg `-0.2079` n `763`
- 4h: commodity avg `0.0916` n `12`; crypto_alt avg `1.1973` n `229`; crypto_major avg `2.3309` n `8`; equity avg `1.8601` n `88`; fx avg `0.0214` n `6`; index avg `0.3221` n `25`; metal avg `0.8349` n `20`; unknown avg `-0.088` n `763`
- 24h: commodity avg `-0.3203` n `12`; crypto_alt avg `3.3031` n `228`; crypto_major avg `4.4856` n `8`; equity avg `0.2185` n `88`; fx avg `-0.0729` n `6`; index avg `-0.1409` n `25`; metal avg `0.7958` n `20`; unknown avg `1.8268` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
