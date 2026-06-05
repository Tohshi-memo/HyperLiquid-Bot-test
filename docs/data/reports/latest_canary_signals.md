# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T02:37:25.291253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.0804` n `228`; crypto_major avg `0.074` n `8`; equity avg `0.0728` n `74`; fx avg `-0.0115` n `6`; index avg `0.0276` n `23`; metal avg `-0.1467` n `18`; unknown avg `1.3115` n `424`
- 1h: commodity avg `0.1708` n `12`; crypto_alt avg `-0.9681` n `228`; crypto_major avg `-0.7435` n `8`; equity avg `0.416` n `74`; fx avg `-0.0136` n `6`; index avg `0.1985` n `23`; metal avg `-0.0995` n `18`; unknown avg `1.0875` n `424`
- 4h: commodity avg `0.1131` n `12`; crypto_alt avg `-0.2682` n `228`; crypto_major avg `-0.0798` n `8`; equity avg `-0.4526` n `74`; fx avg `0.1289` n `6`; index avg `-0.5086` n `23`; metal avg `-0.9675` n `18`; unknown avg `1.1265` n `424`
- 24h: commodity avg `-0.067` n `12`; crypto_alt avg `-3.4271` n `228`; crypto_major avg `-2.6852` n `8`; equity avg `-0.6468` n `73`; fx avg `0.1958` n `6`; index avg `-0.1272` n `23`; metal avg `-0.3541` n `18`; unknown avg `0.2681` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
