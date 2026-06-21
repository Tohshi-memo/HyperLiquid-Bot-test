# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T18:07:26.465558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.2645` n `228`; crypto_major avg `-0.2432` n `8`; equity avg `-0.0512` n `78`; fx avg `0.0126` n `6`; index avg `-0.0076` n `23`; metal avg `-0.1015` n `18`; unknown avg `-0.1721` n `702`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `-0.5023` n `228`; crypto_major avg `-0.4197` n `8`; equity avg `-0.0768` n `78`; fx avg `0.0047` n `6`; index avg `-0.0195` n `23`; metal avg `-0.0785` n `18`; unknown avg `0.1318` n `702`
- 4h: commodity avg `0.1768` n `12`; crypto_alt avg `-0.2195` n `228`; crypto_major avg `-0.0778` n `8`; equity avg `-0.0329` n `78`; fx avg `-0.0814` n `6`; index avg `-0.0284` n `23`; metal avg `-0.0943` n `18`; unknown avg `-0.8778` n `702`
- 24h: commodity avg `0.1453` n `12`; crypto_alt avg `1.1806` n `228`; crypto_major avg `0.1249` n `8`; equity avg `0.3973` n `78`; fx avg `-0.0661` n `6`; index avg `0.0258` n `23`; metal avg `-0.0848` n `18`; unknown avg `-0.3953` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
