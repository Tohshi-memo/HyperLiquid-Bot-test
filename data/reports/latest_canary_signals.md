# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T03:22:33.529704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0054` n `230`; crypto_major avg `0.0296` n `8`; equity avg `0.0937` n `100`; fx avg `-0.0047` n `6`; index avg `0.0436` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0808` n `775`
- 1h: commodity avg `-0.0648` n `12`; crypto_alt avg `0.0107` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `0.2018` n `100`; fx avg `-0.0298` n `6`; index avg `0.0557` n `25`; metal avg `-0.1029` n `20`; unknown avg `0.1454` n `775`
- 4h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0007` n `230`; crypto_major avg `-0.3581` n `8`; equity avg `-0.1052` n `100`; fx avg `0.0934` n `6`; index avg `-0.0807` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0319` n `775`
- 24h: commodity avg `-0.4635` n `12`; crypto_alt avg `1.2652` n `230`; crypto_major avg `1.1908` n `8`; equity avg `0.8103` n `100`; fx avg `0.1261` n `6`; index avg `0.1082` n `25`; metal avg `0.3475` n `20`; unknown avg `-0.0326` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
