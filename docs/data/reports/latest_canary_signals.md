# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T06:52:25.332577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1576` n `12`; crypto_alt avg `-0.198` n `228`; crypto_major avg `-0.3702` n `8`; equity avg `-0.0132` n `72`; fx avg `-0.0111` n `6`; index avg `-0.0108` n `23`; metal avg `-0.0513` n `18`; unknown avg `0.0707` n `420`
- 1h: commodity avg `0.1018` n `12`; crypto_alt avg `0.5108` n `228`; crypto_major avg `0.1076` n `8`; equity avg `0.1664` n `72`; fx avg `0.0143` n `6`; index avg `0.029` n `23`; metal avg `-0.21` n `18`; unknown avg `-0.1619` n `410`
- 4h: commodity avg `0.2791` n `12`; crypto_alt avg `2.0789` n `228`; crypto_major avg `0.9935` n `8`; equity avg `0.4469` n `72`; fx avg `0.0501` n `6`; index avg `0.0342` n `23`; metal avg `-0.4307` n `18`; unknown avg `0.5133` n `410`
- 24h: commodity avg `1.0569` n `12`; crypto_alt avg `-1.0941` n `228`; crypto_major avg `-3.5311` n `8`; equity avg `0.958` n `72`; fx avg `0.0185` n `6`; index avg `1.112` n `23`; metal avg `-1.6098` n `18`; unknown avg `-0.7754` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
