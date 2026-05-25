# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T16:22:15.609965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0876` n `12`; crypto_alt avg `-0.0477` n `228`; crypto_major avg `-0.0964` n `8`; equity avg `-0.0643` n `67`; fx avg `0.0267` n `6`; index avg `-0.0132` n `23`; metal avg `0.0078` n `18`; unknown avg `0.3819` n `405`
- 1h: commodity avg `0.1403` n `12`; crypto_alt avg `0.0852` n `228`; crypto_major avg `-0.1498` n `8`; equity avg `-0.1138` n `67`; fx avg `-0.0085` n `6`; index avg `0.0093` n `23`; metal avg `-0.1092` n `18`; unknown avg `0.906` n `405`
- 4h: commodity avg `0.0698` n `12`; crypto_alt avg `0.798` n `228`; crypto_major avg `-0.0371` n `8`; equity avg `-0.0007` n `67`; fx avg `-0.0266` n `6`; index avg `0.0825` n `23`; metal avg `0.5434` n `18`; unknown avg `0.9377` n `405`
- 24h: commodity avg `-0.4815` n `12`; crypto_alt avg `1.8409` n `228`; crypto_major avg `0.4124` n `8`; equity avg `0.8862` n `67`; fx avg `-0.0226` n `6`; index avg `0.5095` n `23`; metal avg `1.3768` n `18`; unknown avg `1.896` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
