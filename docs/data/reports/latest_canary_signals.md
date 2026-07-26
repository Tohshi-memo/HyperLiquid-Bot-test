# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T22:22:30.128997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `0.1016` n `230`; crypto_major avg `0.0967` n `8`; equity avg `0.0937` n `100`; fx avg `-0.0052` n `6`; index avg `0.02` n `25`; metal avg `0.0085` n `20`; unknown avg `0.1036` n `775`
- 1h: commodity avg `-0.4587` n `12`; crypto_alt avg `0.765` n `230`; crypto_major avg `0.6667` n `8`; equity avg `0.3924` n `100`; fx avg `-0.0011` n `6`; index avg `0.1222` n `25`; metal avg `0.1874` n `20`; unknown avg `0.0601` n `775`
- 4h: commodity avg `-0.3365` n `12`; crypto_alt avg `0.7025` n `230`; crypto_major avg `0.6637` n `8`; equity avg `0.412` n `100`; fx avg `0.02` n `6`; index avg `0.0816` n `25`; metal avg `0.2216` n `20`; unknown avg `-0.262` n `775`
- 24h: commodity avg `-0.7269` n `12`; crypto_alt avg `1.4753` n `230`; crypto_major avg `1.6051` n `8`; equity avg `1.0211` n `100`; fx avg `0.048` n `6`; index avg `0.2137` n `25`; metal avg `0.4054` n `20`; unknown avg `0.0927` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
