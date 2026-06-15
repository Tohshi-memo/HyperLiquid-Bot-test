# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T10:37:34.917983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0047` n `228`; crypto_major avg `0.0839` n `8`; equity avg `0.0163` n `74`; fx avg `-0.0026` n `6`; index avg `-0.0192` n `23`; metal avg `0.0987` n `18`; unknown avg `-0.029` n `689`
- 1h: commodity avg `0.1776` n `12`; crypto_alt avg `0.3991` n `228`; crypto_major avg `0.6253` n `8`; equity avg `0.0091` n `74`; fx avg `0.0123` n `6`; index avg `0.0217` n `23`; metal avg `0.0296` n `18`; unknown avg `0.0766` n `689`
- 4h: commodity avg `-0.2571` n `12`; crypto_alt avg `0.133` n `228`; crypto_major avg `0.6046` n `8`; equity avg `0.0864` n `74`; fx avg `0.0011` n `6`; index avg `0.2624` n `23`; metal avg `0.6681` n `18`; unknown avg `1.3682` n `689`
- 24h: commodity avg `-1.0438` n `12`; crypto_alt avg `2.8946` n `228`; crypto_major avg `2.9904` n `8`; equity avg `1.3718` n `74`; fx avg `0.0563` n `6`; index avg `0.9014` n `23`; metal avg `2.337` n `18`; unknown avg `1.5074` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
