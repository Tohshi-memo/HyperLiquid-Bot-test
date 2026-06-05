# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T04:37:24.839670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5553` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4674` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `0.3205` n `228`; crypto_major avg `0.3599` n `8`; equity avg `0.0521` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0015` n `23`; metal avg `-0.001` n `18`; unknown avg `0.688` n `424`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `0.4051` n `228`; crypto_major avg `0.1677` n `8`; equity avg `-0.0101` n `74`; fx avg `-0.0135` n `6`; index avg `-0.0452` n `23`; metal avg `-0.0139` n `18`; unknown avg `-0.0616` n `424`
- 4h: commodity avg `0.1474` n `12`; crypto_alt avg `-2.0047` n `228`; crypto_major avg `-1.6176` n `8`; equity avg `-0.0623` n `74`; fx avg `0.057` n `6`; index avg `-0.1502` n `23`; metal avg `-0.5788` n `18`; unknown avg `-0.6697` n `424`
- 24h: commodity avg `-0.2232` n `12`; crypto_alt avg `-5.4078` n `228`; crypto_major avg `-4.8818` n `8`; equity avg `-1.7159` n `73`; fx avg `0.195` n `6`; index avg `-0.6414` n `23`; metal avg `-0.85` n `18`; unknown avg `-0.7908` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
