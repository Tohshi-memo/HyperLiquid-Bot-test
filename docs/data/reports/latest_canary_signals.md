# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T13:57:06.662383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.074` n `230`; crypto_major avg `-0.0645` n `8`; equity avg `0.1876` n `114`; fx avg `-0.0167` n `6`; index avg `0.0458` n `25`; metal avg `0.133` n `20`; unknown avg `0.0217` n `792`
- 1h: commodity avg `-0.0281` n `12`; crypto_alt avg `0.1059` n `230`; crypto_major avg `0.2468` n `8`; equity avg `0.286` n `114`; fx avg `0.0114` n `6`; index avg `0.0691` n `25`; metal avg `0.1148` n `20`; unknown avg `0.0903` n `792`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `0.2983` n `230`; crypto_major avg `0.266` n `8`; equity avg `-0.0694` n `114`; fx avg `-0.0011` n `6`; index avg `0.0331` n `25`; metal avg `0.0683` n `20`; unknown avg `2.0171` n `792`
- 24h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.1208` n `230`; crypto_major avg `0.7881` n `8`; equity avg `1.1854` n `114`; fx avg `0.0067` n `6`; index avg `0.157` n `25`; metal avg `0.2119` n `20`; unknown avg `0.0085` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
