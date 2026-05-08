# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T04:22:20.120466+00:00`
- Correlation status: `ready`
- Asset price records: `613`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1843` n `12`; crypto_alt avg `0.1172` n `228`; crypto_major avg `0.076` n `8`; equity avg `0.0891` n `65`; fx avg `0.0189` n `5`; index avg `0.0246` n `23`; metal avg `-0.0557` n `18`; unknown avg `-0.146` n `365`
- 1h: commodity avg `0.1878` n `12`; crypto_alt avg `0.3988` n `228`; crypto_major avg `0.1023` n `8`; equity avg `0.2402` n `65`; fx avg `0.0481` n `5`; index avg `0.0568` n `23`; metal avg `0.0914` n `18`; unknown avg `-0.2388` n `365`
- 4h: commodity avg `-0.3499` n `12`; crypto_alt avg `0.1276` n `228`; crypto_major avg `-0.3681` n `8`; equity avg `0.3685` n `65`; fx avg `0.0642` n `5`; index avg `0.2035` n `23`; metal avg `0.6801` n `18`; unknown avg `-0.4831` n `365`
- 24h: commodity avg `0.5609` n `12`; crypto_alt avg `2.3217` n `228`; crypto_major avg `-1.1684` n `8`; equity avg `-0.932` n `65`; fx avg `0.2124` n `5`; index avg `-0.5734` n `23`; metal avg `0.5183` n `18`; unknown avg `0.0889` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1287`, n `609`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `609`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1138`, n `605`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1126`, n `605`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `609`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `609`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `605`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `605`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0793`, n `605`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `609`, weak_sample_signal
