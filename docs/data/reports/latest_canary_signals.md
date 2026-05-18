# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T23:52:13.726539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0538` n `228`; crypto_major avg `-0.0736` n `8`; equity avg `-0.0948` n `66`; fx avg `0.0317` n `6`; index avg `-0.0697` n `23`; metal avg `-0.0159` n `18`; unknown avg `0.086` n `383`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.2358` n `228`; crypto_major avg `0.1006` n `8`; equity avg `0.0609` n `66`; fx avg `0.03` n `6`; index avg `-0.0726` n `23`; metal avg `0.2071` n `18`; unknown avg `0.1178` n `383`
- 4h: commodity avg `0.2289` n `12`; crypto_alt avg `0.6321` n `228`; crypto_major avg `0.2734` n `8`; equity avg `0.3934` n `66`; fx avg `0.0212` n `6`; index avg `0.1408` n `23`; metal avg `0.6698` n `18`; unknown avg `-0.0363` n `383`
- 24h: commodity avg `0.5892` n `12`; crypto_alt avg `1.5033` n `228`; crypto_major avg `0.1768` n `8`; equity avg `-0.5427` n `66`; fx avg `0.1756` n `6`; index avg `-0.0404` n `23`; metal avg `1.0455` n `18`; unknown avg `0.2775` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
