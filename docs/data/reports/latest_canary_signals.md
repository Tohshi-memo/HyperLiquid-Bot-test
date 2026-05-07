# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T06:52:19.795149+00:00`
- Correlation status: `ready`
- Asset price records: `527`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2369` n `12`; crypto_alt avg `0.2962` n `228`; crypto_major avg `0.1413` n `8`; equity avg `0.0572` n `65`; fx avg `-0.0453` n `4`; index avg `0.0354` n `23`; metal avg `0.0408` n `18`; unknown avg `-0.0348` n `358`
- 1h: commodity avg `-0.3081` n `12`; crypto_alt avg `0.3989` n `228`; crypto_major avg `0.3723` n `8`; equity avg `0.0482` n `65`; fx avg `-0.0188` n `4`; index avg `0.0554` n `23`; metal avg `0.6008` n `18`; unknown avg `0.0269` n `356`
- 4h: commodity avg `-0.2574` n `12`; crypto_alt avg `1.5149` n `228`; crypto_major avg `0.6496` n `8`; equity avg `0.6262` n `65`; fx avg `-0.0156` n `4`; index avg `0.1973` n `23`; metal avg `0.6206` n `18`; unknown avg `0.3632` n `356`
- 24h: commodity avg `-2.1479` n `7`; crypto_alt avg `1.4622` n `223`; crypto_major avg `-0.5924` n `7`; equity avg `1.658` n `47`; fx avg `-0.0508` n `4`; index avg `1.214` n `6`; metal avg `2.0814` n `7`; unknown avg `1.2423` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `523`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `523`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0839`, n `519`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `519`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0758`, n `519`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `519`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0742`, n `519`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `523`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.07`, n `519`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0694`, n `519`, weak_sample_signal
