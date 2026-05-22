# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T12:22:19.936433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4643` n `12`; crypto_alt avg `-0.0851` n `228`; crypto_major avg `0.0745` n `8`; equity avg `0.1684` n `67`; fx avg `-0.0107` n `6`; index avg `0.0854` n `23`; metal avg `-0.314` n `18`; unknown avg `-0.0052` n `386`
- 1h: commodity avg `-0.9112` n `12`; crypto_alt avg `0.5171` n `228`; crypto_major avg `0.6093` n `8`; equity avg `0.3177` n `67`; fx avg `-0.0113` n `6`; index avg `0.1291` n `23`; metal avg `-0.1938` n `18`; unknown avg `0.1954` n `386`
- 4h: commodity avg `-0.9869` n `12`; crypto_alt avg `0.0132` n `228`; crypto_major avg `0.5281` n `8`; equity avg `-0.4775` n `67`; fx avg `-0.0534` n `6`; index avg `-0.1547` n `23`; metal avg `-0.258` n `18`; unknown avg `-0.3027` n `386`
- 24h: commodity avg `-1.8422` n `12`; crypto_alt avg `2.9672` n `228`; crypto_major avg `1.6338` n `8`; equity avg `1.4936` n `67`; fx avg `0.0941` n `6`; index avg `0.9603` n `23`; metal avg `0.8279` n `18`; unknown avg `1.1851` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0405`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.035`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0333`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0323`, n `668`, weak_sample_signal
