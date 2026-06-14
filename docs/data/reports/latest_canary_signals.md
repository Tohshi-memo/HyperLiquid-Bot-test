# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T16:52:31.341586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.1061` n `228`; crypto_major avg `-0.1469` n `8`; equity avg `-0.0528` n `74`; fx avg `0.0028` n `6`; index avg `-0.0269` n `23`; metal avg `0.0045` n `18`; unknown avg `0.0946` n `645`
- 1h: commodity avg `-0.1727` n `12`; crypto_alt avg `0.1334` n `228`; crypto_major avg `0.0005` n `8`; equity avg `-0.092` n `74`; fx avg `0.0034` n `6`; index avg `-0.0345` n `23`; metal avg `0.0469` n `18`; unknown avg `0.2902` n `645`
- 4h: commodity avg `0.0732` n `12`; crypto_alt avg `-0.3201` n `228`; crypto_major avg `-0.3553` n `8`; equity avg `-0.0821` n `74`; fx avg `-0.0338` n `6`; index avg `0.04` n `23`; metal avg `-0.0547` n `18`; unknown avg `0.1736` n `645`
- 24h: commodity avg `-0.2862` n `12`; crypto_alt avg `-1.0165` n `228`; crypto_major avg `-0.3669` n `8`; equity avg `0.562` n `74`; fx avg `-0.0047` n `6`; index avg `0.2186` n `23`; metal avg `-0.0171` n `18`; unknown avg `1.7243` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
