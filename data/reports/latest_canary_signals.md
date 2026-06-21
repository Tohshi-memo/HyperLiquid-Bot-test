# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T03:07:28.230529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0852` n `228`; crypto_major avg `-0.0638` n `8`; equity avg `-0.0001` n `78`; fx avg `0.0038` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0006` n `18`; unknown avg `-0.0101` n `702`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.1445` n `228`; crypto_major avg `-0.1676` n `8`; equity avg `-0.0056` n `78`; fx avg `0.0026` n `6`; index avg `-0.0024` n `23`; metal avg `0.0089` n `18`; unknown avg `0.1165` n `702`
- 4h: commodity avg `0.0117` n `12`; crypto_alt avg `0.1689` n `228`; crypto_major avg `-0.349` n `8`; equity avg `-0.0003` n `78`; fx avg `-0.0075` n `6`; index avg `-0.035` n `23`; metal avg `-0.0146` n `18`; unknown avg `1.3023` n `701`
- 24h: commodity avg `0.1741` n `12`; crypto_alt avg `1.7554` n `228`; crypto_major avg `1.5819` n `8`; equity avg `0.4202` n `78`; fx avg `0.0354` n `6`; index avg `-0.0207` n `23`; metal avg `0.0174` n `18`; unknown avg `1.7086` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
