# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T05:37:17.489000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0465` n `228`; crypto_major avg `-0.0508` n `8`; equity avg `-0.0475` n `67`; fx avg `-0.0135` n `6`; index avg `0.0263` n `23`; metal avg `0.0163` n `18`; unknown avg `0.1107` n `396`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.4541` n `228`; crypto_major avg `-0.0554` n `8`; equity avg `-0.0035` n `67`; fx avg `-0.0104` n `6`; index avg `0.0275` n `23`; metal avg `0.0276` n `18`; unknown avg `-0.0764` n `396`
- 4h: commodity avg `-0.1932` n `12`; crypto_alt avg `-0.9695` n `228`; crypto_major avg `-0.4404` n `8`; equity avg `0.0194` n `67`; fx avg `-0.0111` n `6`; index avg `0.069` n `23`; metal avg `0.0693` n `18`; unknown avg `-0.5567` n `396`
- 24h: commodity avg `-3.0133` n `12`; crypto_alt avg `1.7085` n `228`; crypto_major avg `2.352` n `8`; equity avg `2.3109` n `67`; fx avg `0.0276` n `6`; index avg `1.2437` n `23`; metal avg `1.2269` n `18`; unknown avg `1.8017` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
