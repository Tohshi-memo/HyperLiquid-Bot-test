# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T16:22:21.435942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4309` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0519` n `12`; crypto_alt avg `-0.197` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `-0.0636` n `67`; fx avg `0.0048` n `6`; index avg `-0.0104` n `23`; metal avg `-0.0503` n `18`; unknown avg `-0.1057` n `386`
- 1h: commodity avg `-0.3024` n `12`; crypto_alt avg `-0.0496` n `228`; crypto_major avg `-0.257` n `8`; equity avg `0.0046` n `67`; fx avg `0.0273` n `6`; index avg `0.0463` n `23`; metal avg `0.0883` n `18`; unknown avg `-0.5271` n `386`
- 4h: commodity avg `-0.2037` n `12`; crypto_alt avg `-1.0573` n `228`; crypto_major avg `-1.0822` n `8`; equity avg `-0.1303` n `67`; fx avg `0.0396` n `6`; index avg `0.3487` n `23`; metal avg `-0.0896` n `18`; unknown avg `0.0476` n `386`
- 24h: commodity avg `-1.9945` n `12`; crypto_alt avg `0.9069` n `228`; crypto_major avg `-0.3267` n `8`; equity avg `0.79` n `67`; fx avg `0.1648` n `6`; index avg `1.2108` n `23`; metal avg `-0.2258` n `18`; unknown avg `-0.8616` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0387`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.036`, n `668`, weak_sample_signal
