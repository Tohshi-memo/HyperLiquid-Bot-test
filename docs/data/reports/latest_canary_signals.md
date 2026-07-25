# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T14:37:31.200558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.0587` n `230`; crypto_major avg `0.1214` n `8`; equity avg `0.0352` n `100`; fx avg `0.0061` n `6`; index avg `0.0045` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.1244` n `774`
- 1h: commodity avg `-0.3644` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `0.0256` n `8`; equity avg `0.0154` n `100`; fx avg `-0.0027` n `6`; index avg `0.0128` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0245` n `774`
- 4h: commodity avg `-0.4383` n `12`; crypto_alt avg `0.2948` n `230`; crypto_major avg `0.2695` n `8`; equity avg `0.0263` n `100`; fx avg `-0.0137` n `6`; index avg `0.0104` n `25`; metal avg `0.0148` n `20`; unknown avg `-0.0903` n `774`
- 24h: commodity avg `-0.5719` n `12`; crypto_alt avg `0.2257` n `230`; crypto_major avg `0.4758` n `8`; equity avg `-0.2668` n `100`; fx avg `-0.0107` n `6`; index avg `0.024` n `25`; metal avg `-0.0177` n `20`; unknown avg `13.1813` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.124`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1081`, n `666`, weak_sample_signal
